import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/{}".format(poi['EntityId'])
        return "Last known location for {}".format(poi['EntityId'])

# Only render the signs with the filter string (stored in environment variable
# RENDER_SIGNS_FILTER) in them. If RENDER_SIGNS_FILTER is blank or unset,
# render all signs. RENDER_SIGNS_FILTER defaults to "-- RENDER --" for historic
# reasons, but also so that people can have secret bases and to keep the render
# fairly clean.
def signFilter(poi):
    # Because of how Overviewer reads this file, we must "import os" again here.
    import os
    if poi['id'] in ['Sign', 'minecraft:sign']:
        sign_filter_string = os.environ.get('RENDER_SIGNS_FILTER', "")
        render_all_signs = len(sign_filter_string) == 0
        if render_all_signs or sign_filter_string in poi.values():
        	if len(poi['Text1']) > 0 or len(poi['Text2']) > 0 or len(poi['Text3']) > 0 or len(poi['Text4']) > 0: # filter out empty signs
            return "<br />".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])


worlds["world"] = "/home/minecraft/server/world"
outputdir = "/home/minecraft/render"
texturepath = "/home/minecraft/{}.jar".format(os.environ['MINECRAFT_VERSION'])
processes = 10

markers = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Signs", filterFunction=signFilter)
]

renders["normalrender"] = {
    "world": "world",
    "title": "Minecraft Quarantaine",
	"rendermode": smooth_lighting,
    "dimension": "overworld",
}