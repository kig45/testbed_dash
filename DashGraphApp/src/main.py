import sys
import dash
import dash_bootstrap_components as dbc
from pathlib import Path

from DashGraphApp.src import graph
from DashGraphApp.src import view
from DashGraphApp.src import layout


app = dash.Dash(assets_folder=Path(__file__).parent.parent / "assets")
app.layout = layout.get_app_layout(list(graph.graph.nodes))


@dash.callback(
    dash.Output(component_id="sel-leaf", component_property="options"),
    dash.Input(component_id="sel-root", component_property="value"),
)
def update_leafs(sel_root):
    return [""] + list(graph.get_descendants(sel_root))

dash.clientside_callback(
    dash.ClientsideFunction(
        namespace='clientside',
        function_name='request_full_screen'
    ),
    dash.Input('fullscreen-graph', 'n_clicks'),
    dash.Input('fullscreen-short-tree', 'n_clicks'),
    dash.Input('fullscreen-flat-tree', 'n_clicks'),
)

@dash.callback(
    [
        dash.Output(component_id="view-graph", component_property="figure"),
        dash.Output(component_id="view-short-tree", component_property="figure"),
        dash.Output(component_id="view-flat-tree", component_property="figure"),
    ],
    [
        dash.Input(component_id="sel-root", component_property="value"),
        dash.Input(component_id="sel-leaf", component_property="value")
    ],
)
def update_graph(sel_root, sel_leaf):
    app.logger.warning(f"Searching subgraph from {sel_root} to {sel_leaf}")
    subgraph = graph.get_subgraph(sel_root, sel_leaf)
    app.logger.warning(f"Found subgraph: {subgraph}")
    app.logger.warning(f"Searching simplified subgraph from {sel_root} to {sel_leaf}")
    subtree_shortest = graph.simplify_graph(subgraph, sel_root)
    app.logger.warning(f"Found subgraph: {subgraph}")
    return [
        view.get_graph(subgraph),
        view.get_shortest_tree(subtree_shortest),
        view.get_flat_tree(subtree_shortest)
    ]


def main():
    return app.run()


if __name__ == "__main__":
    sys.exit(main())
