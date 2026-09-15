from datasets import load_dataset
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
import scipy as sp


# Access the CSV files
classes_df = pd.read_csv("data/elliptic_txs_classes.csv")
edges_df = pd.read_csv("data/elliptic_txs_edgelist.csv")

main_graph = nx.from_pandas_edgelist(edges_df,source="txId1",target="txId2",create_using=nx.DiGraph())

lables = classes_df.set_index("txId")["class"].to_dict()

nx.set_node_attributes(main_graph,lables,"class")

node_num = main_graph.number_of_nodes()
edge_num = main_graph.number_of_edges()
density = nx.density(main_graph)
is_directed = main_graph.is_directed()

in_degree = dict(main_graph.in_degree())
out_degree = dict(main_graph.out_degree())
degree = dict(main_graph.degree())
plt.figure(figsize=(6,8))
plt.hist(degree,bins=80)
plt.xlabel("degree")
plt.ylabel("count")
plt.savefig(r"data/histogram.png")

pagerank = nx.pagerank(main_graph)
top10 = sorted(pagerank.items(),reverse=True)[:10]

bet = nx.betweenness_centrality(main_graph,k=1000,seed=23)

sample = list(main_graph.nodes())[:1000]

subgraph = main_graph.subgraph(sample)

color_map = {
    1:"red",
    2:"green",
    "unknown": "gray"
}

node_colors = []

for i in subgraph.nodes:
    node_colors.append(color_map.get(main_graph.nodes[i]["class"],"black"))

plt.figure(figsize=(8,8))
nx.draw_networkx(subgraph,node_color=node_colors[:1000],with_labels=True)
plt.show()
plt.savefig(r"data/graph.png")

result_df = pd.DataFrame({
            "txId": list(main_graph.nodes()),
            "Degree" : pd.Series(degree),
            "InDegree" : pd.Series(in_degree),
            "outDgree" : pd.Series(out_degree),
            "Between" : pd.Series(bet),
            "PageRank" : pd.Series(pagerank)
})

result_df = result_df.merge(classes_df,on="txId",how="left")
result_df.to_csv(r"data/result_elliptic_bitcoin_analyse.csv",index=False)
