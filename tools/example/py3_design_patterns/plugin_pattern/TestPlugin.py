# coding: utf8
import os


# 找到Plugins中所有插件名称
def getPlugin():
    path = os.path.split(os.path.realpath(__file__))[0]
    plugins = os.listdir(path + '/Plugins/')
    fil = lambda str: (True, False)[str[-3:] == 'pyc' or str.find('__init__.py') != -1]
    return filter(fil, plugins)


if __name__ == "__main__":
    # 遍历所有插件
    for plugin in getPlugin():
        # Get Plugin File Name
        pluginName = os.path.splitext(plugin)[0]
        # Load Plugin
        plugin = __import__("Plugins." + pluginName, fromlist=[pluginName])
        myplugin = getattr(plugin, "A")
        # Get Plugin Object
        p = myplugin()
        # Invoke Plugin Method
        p.process()
