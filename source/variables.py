defaultGraph = """<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.css" type="text/css" />
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis-network.min.js"> </script>
<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
<style type="text/css">
        #mynetwork {
            width: 1000px;
            height: 500px;
            background-color: #ffffff;
            border: 0px solid lightgray;
            position: relative;
            float: left;
        }
</style>
</head>
<body>
<div id = "mynetwork"></div>
<script type="text/javascript">
    // initialize global variables.
    var edges;
    var nodes;
    var network; 
    var container;
    var options, data;
    // This method is responsible for drawing the graph, returns the drawn network
    function drawGraph() {
        var container = document.getElementById('mynetwork');
        // parsing and collecting nodes and edges from the python
        nodes = new vis.DataSet([{"id": 0, "label": 0, "shape": "dot", "size": 10}, {"group": 1, "id": 1, "label": 1, "shape": "dot", "size": 10, "title": "Number 1"}, {"id": 9, "label": 9, "shape": "dot", "size": 10}, {"id": 2, "label": 2, "shape": "dot", "size": 10}, {"group": 10, "id": 3, "label": 3, "shape": "dot", "size": 10, "title": "I belong to a different group!"}, {"id": 4, "label": 4, "shape": "dot", "size": 10}, {"id": 5, "label": 5, "shape": "dot", "size": 10}, {"id": 6, "label": 6, "shape": "dot", "size": 10}, {"id": 7, "label": 7, "shape": "dot", "size": 10}, {"id": 8, "label": 8, "shape": "dot", "size": 10}, {"group": 2, "id": 20, "label": 20, "shape": "dot", "size": 20, "title": "couple"}, {"group": 2, "id": 21, "label": 21, "shape": "dot", "size": 15, "title": "couple"}, {"group": 3, "id": 25, "label": "lonely", "shape": "dot", "size": 25, "title": "lonely node"}]);
        edges = new vis.DataSet([{"from": 0, "to": 1, "weight": 1}, {"from": 0, "to": 9, "weight": 1}, {"from": 1, "to": 2, "weight": 1}, {"from": 2, "to": 3, "weight": 1}, {"from": 3, "to": 4, "weight": 1}, {"from": 4, "to": 5, "weight": 1}, {"from": 5, "to": 6, "weight": 1}, {"from": 6, "to": 7, "weight": 1}, {"from": 7, "to": 8, "weight": 1}, {"from": 8, "to": 9, "weight": 1}, {"from": 20, "to": 21, "weight": 5}]);
        // adding nodes and edges to the graph
        data = {nodes: nodes, edges: edges};
        var options = {
    "configure": {
        "enabled": false
    },
    "edges": {
        "color": {
            "inherit": true
        },
        "smooth": {
            "enabled": false,
            "type": "continuous"
        }
    },
    "interaction": {
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
    },
    "physics": {
        "enabled": true,
        "stabilization": {
            "enabled": true,
            "fit": true,
            "iterations": 1000,
            "onlyDynamicEdges": false,
            "updateInterval": 50
        }
    }
};
        
        

        

        network = new vis.Network(container, data, options);

        


        

        return network;

    }

    drawGraph();

</script>
</body>
</html>"""
