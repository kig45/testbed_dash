import networkx as nx
import plotly.graph_objects as go


def get_graph(gra: nx.DiGraph) -> go.Figure:
    fig = go.Figure(layout=go.Layout(autosize=False, margin=go.layout.Margin(b=0, l=0, r=0, t=0)))
    pos = nx.multipartite_layout(gra, "layer")
    lsNX = [p[0] for p in pos.values()]
    lsNY = [p[1] for p in pos.values()]
    lsNLabel = [p for p in pos.keys()]
    lsEX = []
    lsEY = []
    for e_in, e_out in gra.edges():
        lsEX += [pos[e_in][0], pos[e_out][0]]
        lsEY += [pos[e_in][1], pos[e_out][1]]

    fig.add_trace(go.Scatter(x=lsNX, y=lsNY, mode='markers', text=lsNLabel))
    fig.add_trace(go.Scatter(x=lsEX, y=lsEY, mode='lines'))
    return fig


def get_shortest_tree(gra: nx.DiGraph) -> go.Figure:
    fig = go.Figure(layout=go.Layout(autosize=False, margin=go.layout.Margin(b=0, l=0, r=0, t=0)))

    lsVal = []
    lsLabel = []
    lsParent = []
    for n, data in gra.nodes.data():
        lsVal += [data["layer"]]
        lsLabel += [n]
        lsE = [e_in for e_in, _ in gra.in_edges(n)]
        lsParent += [lsE[0]] if 0 < data["layer"] and len(lsE) > 0 else [""]

    fig.add_trace(go.Treemap(labels=lsLabel, values=lsVal, parents=lsParent))
    return fig

def get_flat_tree(gra: nx.DiGraph) -> go.Figure:
    fig = go.Figure(layout=go.Layout(autosize=False, margin=go.layout.Margin(b=0, l=0, r=0, t=0)))

    lsLabel = [n for n in gra.nodes()]
    lsVal = [data["layer"] for _, data in gra.nodes(True)]
    lsParent = ["" for _ in range(len(lsVal))]
    fig.add_trace(go.Treemap(labels=lsLabel, values=lsVal, parents=lsParent))
    return fig