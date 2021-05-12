# autoinsert-plugin

The plugin works with the cadnano2-pyqt5: feel free to modify it to other versions- it should be relatively straight forward.

Clone the autoinsert repository: git clone git@github.com:Ashwinkarthick/autoinsert_plugin.git to the plugins folder inside the cadnano2-pyqt5 folder.
You can also download and manually place it inside cadnano2-pyqt5/plugins

One can also create a symbolic link if preferred.

The initial code was written by Juhana Kommeri as part of his master thesis "Computer-aided design software for custom nucleic acid nanostructures" in Aalto University (https://aaltodoc.aalto.fi/handle/123456789/23326).

The code was improved with help from Jaishankar Natarajan.

Autoskip plugin is available at https://github.com/Ashwinkarthick/autoskip_plugin

# How to use

The plugin has three options
1. target bps between insertions - number of base pairs between each insertion site.
2. number of insertions          - introduces specified number of insertions at every target site
3. minimum dist from edge        - distance from the initial edge crossover between the first two helices. 

Depending on the number of insertions, the script takes between few seconds to few minutes to run.
