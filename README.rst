.. image:: https://github.com/dfguerrerom/voila-sepal-ui/actions/workflows/release.yml/badge.svg
   :target: https://github.com/dfguerrerom/voila-sepal-ui/actions/workflows/release.yml
   :alt: Upload Python Package


voila-sepal-ui
==============

This is a fork of the voila-vuetify project original project. The purpose of this fork is to create a template for the sepal-ui project.

Installation
============

.. code-block:: bash

   git clone https://github.com/dfguerrerom/voila-sepal-ui.git
   cd voila-sepal-ui
   pip install .


Usage
=====

To use the `sepal-ui` template, just pass `--template=sepal-ui-base` to the `voila` command line.

.. code-block:: bash

   voila app.ipynb --template=sepal-ui-base --show_tracebacks=True


Alternatively, you can also set the template definition in the notebook metadata to use the `sepal-u-basei` template. Open the notebook as a text file and add the following metadata:

.. code-block:: json

   "voila" : {
      "template" : "sepal-ui-base"
   }

You can also set the title of the tool by adding the following metadata:

.. code-block:: json

   "title" : "My geospatial-ui tool"
