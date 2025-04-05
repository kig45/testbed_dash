import dash
import dash_bootstrap_components as dbc

def get_app_layout(ls_nodes):
    return [
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("About", href="#")),
            ],
            brand="Dash Tree Graph",
            brand_href="#",
        ),
        dbc.Container([
            dash.html.Div(id="log"),
            dash.html.Br(),
            dash.dcc.Loading([
                dash.html.Div([
                    dbc.Row([
                        dbc.Label("Select Root FrameWork", html_for="sel-root", width=2),
                        dbc.Col(dbc.Select([""] + ls_nodes, value="", required=False, id="sel-root"), width=2)
                    ]),
                    dbc.Row([
                        dbc.Label("Select Leaf FrameWork", html_for="sel-leaf", width=2),
                        dbc.Col(dbc.Select([""] + ls_nodes, value="", required=False, id="sel-leaf"), width=2)
                    ]),
                ]),
            ], type="default"),
            dash.html.Br(),
            dash.html.Div([
                dash.html.H2("Layered Graph View"),
                dbc.Row([
                    dbc.Col(dbc.Button("Fullscreen", id="fullscreen-graph", color="primary", className="me-1", n_clicks=0)),
                    dbc.Col(dash.html.P("Every child nodes accessibles from selected Root are shown. The number of jumps to get from root to node is shown as X axis"))
                ]),
                dash.dcc.Loading(dash.dcc.Graph(figure={}, id="view-graph", config={"displaylogo": False, "watermark": False}), type="default"),
            ]),
            dash.html.Br(),
            dash.html.Div([
                dash.dcc.Loading(type="default", children=dash.html.Div(id="loading-view-short-tree")),
                dash.html.H2("Recursive Tree View"),
                dbc.Row([
                    dbc.Col(dbc.Button("Fullscreen", id="fullscreen-short-tree", color="primary", className="me-1", n_clicks=0)),
                    dbc.Col(dash.html.P("Every child nodes accessibles from selected Root are shown. Since anode may appear from different Paths, they may be repeated")),
                ]),
                dash.dcc.Loading(dash.dcc.Graph(figure={}, id="view-short-tree", config={"displaylogo": False, "watermark": False}), type="default"),
            ]),
            dash.html.Br(),
            dash.html.Div([
                dash.dcc.Loading(type="default", children=dash.html.Div(id="loading-view-flat-tree")),
                dash.html.H2("Flattened Tree View"),
                dbc.Row([
                    dbc.Col(dbc.Button("Fullscreen", id="fullscreen-flat-tree", color="primary", className="me-1", n_clicks=0)),
                    dbc.Col(dash.html.P("Every child nodes accessibles from selected Root are shown flattened")),
                ]),
                dash.dcc.Loading(dash.dcc.Graph(figure={}, id="view-flat-tree", config={"displaylogo": False, "watermark": False}), type="default"),
            ])
        ])
    ]
