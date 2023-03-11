import pandas as pd
import pandas as pd
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
from joblib import load
import shap
import plotly.graph_objects as go

app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])
modelo= load('assets/randomForest.joblib') 


app.layout = html.Div(children=[

    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Adrián Landaverde Nava", href="#")),
            dbc.NavItem(dbc.NavLink("Cristian Gonzaga López", href="#")),
            dbc.NavItem(dbc.NavLink("Yanina De Luna Ocampo", href="#")),
            dbc.NavItem(dbc.NavLink("Juan Pablo Minoru Sainz Takata", href="#")),
            ],
        
        brand="Dermatology Analysis",
        brand_href="#",
        color="primary",
        dark=True,
        fluid=True),
    
    html.Br(),

    dbc.Col([
    
        dbc.Row([
            dbc.Col(html.H3("Variables"), width=7),
        
            dbc.Col(html.H3("Prediction"),width=5),
        ]),
        

        dbc.Row([


            dbc.Col([
                dbc.Row([
    
                    dbc.Col(html.P("erythema: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="erythema", value=3), width=3),


                    dbc.Col(html.P("scaling: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="scaling", value=2), width=3),


                    dbc.Col(html.P("definite_borders: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="definite_borders", value=0), width=3),


                    dbc.Col(html.P("itching: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="itching", value=0), width=3),


                    dbc.Col(html.P("koebner_phenomenon: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="koebner_phenomenon", value=0), width=3),


                    dbc.Col(html.P("polygonal_papules: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="polygonal_papules", value=0), width=3),


                    dbc.Col(html.P("follicular_papules: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="follicular_papules", value=0), width=3),


                    dbc.Col(html.P("oral_mucosal_involvement: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="oral_mucosal_involvement", value=0), width=3),


                    dbc.Col(html.P("knee_and_elbow_involvement: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="knee_and_elbow_involvement", value=0), width=3),


                    dbc.Col(html.P("scalp_involvement: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="scalp_involvement", value=0), width=3),


                    dbc.Col(html.P("family_history: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="family_history", value=0), width=3),


                    dbc.Col(html.P("melanin_incontinence: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="melanin_incontinence", value=0), width=3),


                    dbc.Col(html.P("eosinophils_in_the_infiltrate: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="eosinophils_in_the_infiltrate", value=0), width=3),


                    dbc.Col(html.P("pnl_infiltrate: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="pnl_infiltrate", value=2), width=3),


                    dbc.Col(html.P("fibrosis_of_the_papillary_dermis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="fibrosis_of_the_papillary_dermis", value=0), width=3),


                    dbc.Col(html.P("exocytosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="exocytosis", value=0), width=3),


                    dbc.Col(html.P("acanthosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="acanthosis", value=2), width=3)
                   
                ])
            ], width=3),

            dbc.Col([
                dbc.Row([
                    dbc.Col(html.P("hyperkeratosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="hyperkeratosis", value=0), width=3),


                    dbc.Col(html.P("parakeratosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="parakeratosis", value=1), width=3),


                    dbc.Col(html.P("clubbing_of_the_rete_ridges: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="clubbing_of_the_rete_ridges", value=0), width=3),


                    dbc.Col(html.P("elongation_of_the_rete_ridges: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="elongation_of_the_rete_ridges", value=2), width=3),


                    dbc.Col(html.P("thinning_of_the_suprapapillary_epidermis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="thinning_of_the_suprapapillary_epidermis", value=2), width=3),


                    dbc.Col(html.P("spongiform_pustule: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="spongiform_pustule", value=0), width=3),


                    dbc.Col(html.P("munro_microabcess: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="munro_microabcess", value=0), width=3),


                    dbc.Col(html.P("focal_hypergranulosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="focal_hypergranulosis", value=0), width=3),


                    dbc.Col(html.P("disappearance_of_the_granular_layer: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="disappearance_of_the_granular_layer", value=0), width=3),


                    dbc.Col(html.P("vacuolisation_and_damage_of_basal_layer: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="vacuolisation_and_damage_of_basal_layer", value=0), width=3),


                    dbc.Col(html.P("spongiosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="spongiosis", value=0), width=3),


                    dbc.Col(html.P("saw-tooth_appearance_of_retes: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="saw-tooth_appearance_of_retes", value=0), width=3),


                    dbc.Col(html.P("follicular_horn_plug: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="follicular_horn_plug", value=0), width=3),


                    dbc.Col(html.P("perifollicular_parakeratosis: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="perifollicular_parakeratosis", value=0), width=3),


                    dbc.Col(html.P("inflammatory_monoluclear_inflitrate: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="inflammatory_monoluclear_inflitrate", value=2), width=3),


                    dbc.Col(html.P("band-like_infiltrate: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=4, step=1, size="sm",
                                    id="band-like_infiltrate", value=0), width=3),


                    dbc.Col(html.P("age: "), width=9),

                    dbc.Col(dbc.Input(type="number", min=0, max=90, step=1, size="sm",
                                    id="age", value=56), width=3)
                ])
            ],width=4),

            dbc.Col([

                html.H4(id="Prediccion_Clase"),

                dbc.Row([
                    dbc.Col(html.P("Probability of having:"), width=5),

                    dbc.Col(dbc.Select(
                            id="select_sick",
                            options=[
                                {"label": "Psoriasis", "value": "0"},
                                {"label": "Seboreic Dermatitis", "value": "1"},
                                {"label": "lichen planus", "value": "2"},
                                {"label": "Pityriasis rosea", "value": "3"},
                                {"label": "Cronic dermatitis", "value": "4"},
                                {"label": "Pityriasis rubra pilaris", "value": "5"},
                            ],value="0", size="sm"
                        ), width=7)
                ]),
                

                dcc.Graph(id="waterfall")

            ])
        ])
    ],style={'margin-right': '20px', 'margin-left': '20px'})
])


@app.callback(Output('Prediccion_Clase', 'children'),
              [Input('erythema', 'value'), Input('scaling', 'value'), Input('definite_borders', 'value'), Input('itching', 'value'), Input('koebner_phenomenon', 'value'), Input('polygonal_papules', 'value'), Input('follicular_papules', 'value'), Input('oral_mucosal_involvement', 'value'), Input('knee_and_elbow_involvement', 'value'), Input('scalp_involvement', 'value'), Input('family_history', 'value'), Input('melanin_incontinence', 'value'), Input('eosinophils_in_the_infiltrate', 'value'), Input('pnl_infiltrate', 'value'), Input('fibrosis_of_the_papillary_dermis', 'value'), Input('exocytosis', 'value'), Input('acanthosis', 'value'), Input('hyperkeratosis', 'value'), Input('parakeratosis', 'value'), Input('clubbing_of_the_rete_ridges', 'value'), Input('elongation_of_the_rete_ridges', 'value'), Input('thinning_of_the_suprapapillary_epidermis', 'value'), Input('spongiform_pustule', 'value'), Input('munro_microabcess', 'value'), Input('focal_hypergranulosis', 'value'), Input('disappearance_of_the_granular_layer', 'value'), Input('vacuolisation_and_damage_of_basal_layer', 'value'), Input('spongiosis', 'value'), Input('saw-tooth_appearance_of_retes', 'value'), Input('follicular_horn_plug', 'value'), Input('perifollicular_parakeratosis', 'value'), Input('inflammatory_monoluclear_inflitrate', 'value'), Input('band-like_infiltrate', 'value'), Input('age', 'value'), ])
def predecir(erythema, scaling, definite_borders, itching, koebner_phenomenon, polygonal_papules, follicular_papules, oral_mucosal_involvement, knee_and_elbow_involvement, scalp_involvement, family_history, melanin_incontinence, eosinophils_in_the_infiltrate, pnl_infiltrate, fibrosis_of_the_papillary_dermis, exocytosis, acanthosis, hyperkeratosis, parakeratosis, clubbing_of_the_rete_ridges, elongation_of_the_rete_ridges, thinning_of_the_suprapapillary_epidermis, spongiform_pustule, munro_microabcess, focal_hypergranulosis, disappearance_of_the_granular_layer, vacuolisation_and_damage_of_basal_layer, spongiosis, saw_tooth_appearance_of_retes, follicular_horn_plug, perifollicular_parakeratosis, inflammatory_monoluclear_inflitrate, band_like_infiltrate, age):
    variables=[erythema, scaling, definite_borders, itching, koebner_phenomenon, polygonal_papules, follicular_papules, oral_mucosal_involvement, knee_and_elbow_involvement, scalp_involvement, family_history, melanin_incontinence, eosinophils_in_the_infiltrate, pnl_infiltrate, fibrosis_of_the_papillary_dermis, exocytosis, acanthosis, hyperkeratosis, parakeratosis, clubbing_of_the_rete_ridges, elongation_of_the_rete_ridges, thinning_of_the_suprapapillary_epidermis, spongiform_pustule, munro_microabcess, focal_hypergranulosis, disappearance_of_the_granular_layer, vacuolisation_and_damage_of_basal_layer, spongiosis, saw_tooth_appearance_of_retes, follicular_horn_plug, perifollicular_parakeratosis, inflammatory_monoluclear_inflitrate, band_like_infiltrate, age]
    X_test=pd.DataFrame(variables).T
    X_test.columns=['erythema', 'scaling', 'definite_borders', 'itching',
       'koebner_phenomenon', 'polygonal_papules', 'follicular_papules',
       'oral_mucosal_involvement', 'knee_and_elbow_involvement',
       'scalp_involvement', 'family_history', 'melanin_incontinence',
       'eosinophils_in_the_infiltrate', 'pnl_infiltrate',
       'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis',
       'hyperkeratosis', 'parakeratosis', 'clubbing_of_the_rete_ridges',
       'elongation_of_the_rete_ridges',
       'thinning_of_the_suprapapillary_epidermis', 'spongiform_pustule',
       'munro_microabcess', 'focal_hypergranulosis',
       'disappearance_of_the_granular_layer',
       'vacuolisation_and_damage_of_basal_layer', 'spongiosis',
       'saw-tooth_appearance_of_retes', 'follicular_horn_plug',
       'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate',
       'band-like_infiltrate', 'age']
    print(X_test)

    prediccion= modelo.predict(X_test)
    print(prediccion)

    dic_values= {1:"psoriasis", 2:"seboreic dermatitis", 3:"lichen planus", 
                 4:"pityriasis rosea", 5:"cronic dermatitis", 6:"pityriasis rubra pilaris"}

    texto="Predicted sickness: "+ dic_values[prediccion[0]]



    return(texto)

@app.callback(Output('waterfall', 'figure'),
              [Input('erythema', 'value'), Input('scaling', 'value'), Input('definite_borders', 'value'), Input('itching', 'value'), Input('koebner_phenomenon', 'value'), Input('polygonal_papules', 'value'), Input('follicular_papules', 'value'), Input('oral_mucosal_involvement', 'value'), Input('knee_and_elbow_involvement', 'value'), Input('scalp_involvement', 'value'), Input('family_history', 'value'), Input('melanin_incontinence', 'value'), Input('eosinophils_in_the_infiltrate', 'value'), Input('pnl_infiltrate', 'value'), Input('fibrosis_of_the_papillary_dermis', 'value'), Input('exocytosis', 'value'), Input('acanthosis', 'value'), Input('hyperkeratosis', 'value'), Input('parakeratosis', 'value'), Input('clubbing_of_the_rete_ridges', 'value'), Input('elongation_of_the_rete_ridges', 'value'), Input('thinning_of_the_suprapapillary_epidermis', 'value'), Input('spongiform_pustule', 'value'), Input('munro_microabcess', 'value'), Input('focal_hypergranulosis', 'value'), Input('disappearance_of_the_granular_layer', 'value'), Input('vacuolisation_and_damage_of_basal_layer', 'value'), Input('spongiosis', 'value'), Input('saw-tooth_appearance_of_retes', 'value'), Input('follicular_horn_plug', 'value'), Input('perifollicular_parakeratosis', 'value'), Input('inflammatory_monoluclear_inflitrate', 'value'), Input('band-like_infiltrate', 'value'), Input('age', 'value'),Input('select_sick','value') ])
def graficar(erythema, scaling, definite_borders, itching, koebner_phenomenon, polygonal_papules, follicular_papules, oral_mucosal_involvement, knee_and_elbow_involvement, scalp_involvement, family_history, melanin_incontinence, eosinophils_in_the_infiltrate, pnl_infiltrate, fibrosis_of_the_papillary_dermis, exocytosis, acanthosis, hyperkeratosis, parakeratosis, clubbing_of_the_rete_ridges, elongation_of_the_rete_ridges, thinning_of_the_suprapapillary_epidermis, spongiform_pustule, munro_microabcess, focal_hypergranulosis, disappearance_of_the_granular_layer, vacuolisation_and_damage_of_basal_layer, spongiosis, saw_tooth_appearance_of_retes, follicular_horn_plug, perifollicular_parakeratosis, inflammatory_monoluclear_inflitrate, band_like_infiltrate, age, clase):
    variables=[erythema, scaling, definite_borders, itching, koebner_phenomenon, polygonal_papules, follicular_papules, oral_mucosal_involvement, knee_and_elbow_involvement, scalp_involvement, family_history, melanin_incontinence, eosinophils_in_the_infiltrate, pnl_infiltrate, fibrosis_of_the_papillary_dermis, exocytosis, acanthosis, hyperkeratosis, parakeratosis, clubbing_of_the_rete_ridges, elongation_of_the_rete_ridges, thinning_of_the_suprapapillary_epidermis, spongiform_pustule, munro_microabcess, focal_hypergranulosis, disappearance_of_the_granular_layer, vacuolisation_and_damage_of_basal_layer, spongiosis, saw_tooth_appearance_of_retes, follicular_horn_plug, perifollicular_parakeratosis, inflammatory_monoluclear_inflitrate, band_like_infiltrate, age]
    X_test=pd.DataFrame(variables).T
    X_test.columns=['erythema', 'scaling', 'definite_borders', 'itching',
       'koebner_phenomenon', 'polygonal_papules', 'follicular_papules',
       'oral_mucosal_involvement', 'knee_and_elbow_involvement',
       'scalp_involvement', 'family_history', 'melanin_incontinence',
       'eosinophils_in_the_infiltrate', 'pnl_infiltrate',
       'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis',
       'hyperkeratosis', 'parakeratosis', 'clubbing_of_the_rete_ridges',
       'elongation_of_the_rete_ridges',
       'thinning_of_the_suprapapillary_epidermis', 'spongiform_pustule',
       'munro_microabcess', 'focal_hypergranulosis',
       'disappearance_of_the_granular_layer',
       'vacuolisation_and_damage_of_basal_layer', 'spongiosis',
       'saw-tooth_appearance_of_retes', 'follicular_horn_plug',
       'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate',
       'band-like_infiltrate', 'age']
    clase=int(clase)

    explainer = shap.TreeExplainer(modelo)
    
    explainer = shap.TreeExplainer(modelo)
    shap_values = explainer.shap_values(X_test)
    df_shap=pd.DataFrame({"Valores":shap_values[clase][0], "Nombres":X_test.columns})
    df_shap["Valores_Abs"]=(df_shap["Valores"]).abs()
    df_shap= df_shap.sort_values(by="Valores_Abs", ascending=False)
    df_shap
    otros=df_shap.iloc[10:]["Valores"].sum()

    data= go.Data([go.Waterfall(
            orientation = "v",
            measure = ["relative"]*10,
            x = ["Others"]+list(df_shap.iloc[:10]["Nombres"].iloc[::-1]),
            textposition = "outside",
            text = [str(round(otros,3))]+list(df_shap.iloc[:10]["Valores"].round(3).iloc[::-1].astype(str)),
            y = [otros]+list(df_shap.iloc[:10]["Valores"].iloc[::-1]),
            connector = {"line":{"color":"rgb(63, 63, 63)"}},
            decreasing = {"marker":{"color":"dodgerBlue"}},
            increasing = {"marker":{"color":"crimson"}},
            base=explainer.expected_value[clase],
        )])
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin={'t': 0}
    )

    fig=go.Figure(data=data, layout=layout)
    fig.update_layout(font=dict(color="white"), height=650)

    return(fig)



    

# -------------------- Run Apps ------------------------
server= app.server
if __name__ == '__main__':
    app.run_server()

