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
##################################################################################
def shade_pct(fips, df, language):
    '''
    Inputs:
        fips: list of county codes
        df: pandas dataframe with language columns 
        language: string-spanish, french or chinese
    Algorigthm:
        initilizes empty lists and determines max percent in language series
        loops through counties by fips
        if county is in dataframe:
            get county pct language speaking
            color based on percentage of max pct
            append color to colors list
        else:
            color grey (#AAAAAA)
    Returns:
        colors: list of colors (hexcode)
    '''
    colors = []
    counties = []
    max_pct = max(df[F'pct_{language}'])
    for county in fips:
        if county in list(df.index):
            pct = df.loc[county][F"pct_{language}"]
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
##################################################################################
def shade_lan(fips, df, other_pct=False):
    '''
    Inputs:
        fips: list of county codes
        df: pandas dataframe with languages columns 
        other_pct: option to compare languages with calculated "other" (default: False)
    Algorigthm:
        initilizes empty lists, language:color codes dictionary, and language list
        loops through county by fip
            if county is in the dataframe:
                set gmaps color to white (#FFFFFF) by default
                initialize plurality language marker to 0
                if other_pct = True:
                    set plurality language as the difference between 100 and the sum of the other languages
                loop through each language
                    get county pct language speaking
                    if pct is larger than plurality pct:
                        set the plurality language to pct
                        set gmaps_color to language's color
                append gmaps_color to colors
            else:
                append grey (#AAAAAA) to colors
    Return:
        colors: list of colors
    '''
    colors = []
    counties = []
    l_colors = {"spanish":"#FF8E00","french":"#006FFF","chinese":"#FF0000"}
    languages = list(l_colors.keys())
    for county in fips:
        if county in list(df.index):
            gmaps_color = "#FFFFFF"
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
##################################################################################
def kwikplt(pop,lan):
    '''
    Inputs:
        pop: list or series of populations
        lan: list or series of language spears as a percent of population
    Algorigthm:
        runs linear regression
        sets min and max population (x coordinates)
        sets min and max percentages (y coordinates)
        creates line element from min and max x and y coordinates
        plots scatter from pop and lan list
        plots line element
    Returns
        None: None
    '''
    from scipy.stats import linregress
    from matplotlib import pyplot as plt
    import matplotlib.lines as mlines
    m,b,r,p,_ = linregress(pop,lan)
    eq_str = "y = {:.2E}*x + {:.2f}".format(m,b)
    r_str = "{:.2f}".format(r)
    p_str = "{:.2E}".format(p)
    min_pop = min(pop)
    max_pop = max(pop)
    min_pct = m*min_pop+b
    max_pct = m*max_pop+b
    l = mlines.Line2D([min_pop,max_pop],[min_pct,max_pct],color='orange', lw=5)
    plt.scatter(pop,lan, s=200, marker='+')
    ax = plt.gca()
    ax.add_line(l)
    return eq_str, r_str, p_str