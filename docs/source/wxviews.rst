# WXViews
=========
Modules, packages and subpackages used to implement the Graphical User Interface for the Low Voltage Tool.

## Core
Main classes that will be used by all Graphical Items

### Engine
.. autoclass:: Engine

### Window
.. autoclass:: LowVoltageTool

## Drawers
Contains modules that tells the Tool how to build the different items.

### Drawer
.. autoclass:: Drawer

### NodeDrawer
.. autoclass:: NodeDrawer

## Items
All graphical items that encapsulates the items from the models package.

### NetworkRepr
.. autoclass:: NetworkRepr

### NodeRepr
.. autoclass:: NodeRepr

## Panels
Main containers of the application.

### Table
Package containing the elements used to implement a table.

#### InputGrid
.. autoclass:: InputGrid

#### OutputGrid
.. autoclass:: OutputGrid

#### TabbedGrid
.. autoclass:: TabbedGrid

### DetailsPanel
.. autoclass:: DetailsPanel

### PaintPanel
.. autoclass:: PaintPanel

### ToolBar
.. autoclass:: ToolBar

## Patterns
Package containing modules to implement some design patterns

### Observer
.. autoclass:: Observer
.. autoclass:: Observable

### Singleton
.. autoclass:: Singleton
