'''
#Map created via:
c = shade_pct(fips_ls, df, "chinese")

fig = gmaps.figure()
pct_layer = gmaps.geojson_layer(counties_geojson, stroke_weight = 0.5,
                                fill_color=c, fill_opacity=0.5)
state_layer = gmaps.geojson_layer(state_geojson, stroke_weight = 2,
                                  fill_opacity=0)
fig.add_layer(pct_layer)
fig.add_layer(state_layer)
fig
'''

def shade_pct(fips, df, language):
    colors = []
    counties = []
    for county in fips:
        if county in list(df.index):
            pct = df.loc[county][F"pct_{language}"]
            max_pct = max(df[F'pct_{language}'])
            p = pct/max_pct
            if p == 1:
                gmaps_color = "#60ff30"
            elif p > 0.75:
                gmaps_color = "#24ffd9"
            elif p > 0.5:
                gmaps_color = "#1c86ff"
            elif p > 0.25:
                gmaps_color = "#4c14ff"
            elif p > 0.1:
                gmaps_color = "#9d10ff"
            elif p > 0:
                gmaps_color = "#ff08b6"
            else:
                gmaps_color = "#ff0000"
                
            colors.append(gmaps_color)  
        else:
            colors.append("#AAAAAA")
    return colors 

def shade_lan(fips, df, other_pct=False):
    colors = []
    counties = []
    l_colors = {"spanish":"#FF8E00","french":"#006FFF","chinese":"#FF0000"}
    languages = list(l_colors.keys())
    for county in fips:
        if county in list(df.index):
            gmaps_color = "#FFFFFF"
            #county_fipps = county["fips"]
            plur_lan = 0
            if other_pct:
                plur_lan = 100-df.loc[county][F"pct_spanish"]+df.loc[county][F"pct_french"]+df.loc[county][F"pct_chinese"]
            for lan in languages: 
                pct = df.loc[county][F"pct_{lan}"]
                if pct > plur_lan:
                    plur_lan = pct
                    gmaps_color = l_colors[lan]
            colors.append(gmaps_color)
        else:
            colors.append("#AAAAAA")
    return colors