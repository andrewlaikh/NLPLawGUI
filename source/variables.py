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


example1 = """
<html>
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
            border: 1px solid lightgray;
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
        nodes = new vis.DataSet([{"color": "blue", "group": 1, "id": "regulation 1913/2005", "label": "regulation 1913/2005", "shape": "dot", "size": 25, "title": "regulation 1913/2005 Neighbors:\u003cbr\u003eregulation 2771/75\u003cbr\u003eregulation 2529/2001\u003cbr\u003eregulation 806/2003\u003cbr\u003eregulation 2759/75\u003cbr\u003eregulation 1365/2000\u003cbr\u003eregulation 1255/1999\u003cbr\u003eregulation 1782/2003\u003cbr\u003eregulation 186/2004\u003cbr\u003eregulation 1254/1999\u003cbr\u003eregulation 2777/75\u003cbr\u003eregulation 1913/2005"}, {"color": "yellow", "group": 2, "id": "regulation 2759/75", "label": "regulation 2759/75", "shape": "dot", "size": 10, "title": "regulation 2759/75 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 2771/75", "label": "regulation 2771/75", "shape": "dot", "size": 10, "title": "regulation 2771/75 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 2777/75", "label": "regulation 2777/75", "shape": "dot", "size": 10, "title": "regulation 2777/75 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 1254/1999", "label": "regulation 1254/1999", "shape": "dot", "size": 10, "title": "regulation 1254/1999 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 1255/1999", "label": "regulation 1255/1999", "shape": "dot", "size": 10, "title": "regulation 1255/1999 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 2529/2001", "label": "regulation 2529/2001", "shape": "dot", "size": 10, "title": "regulation 2529/2001 Neighbors:\u003cbr\u003eregulation 467/2001\u003cbr\u003eregulation 215/2003\u003cbr\u003eregulation 881/2002\u003cbr\u003eregulation 145/2003"}, {"color": "yellow", "group": 2, "id": "regulation 1365/2000", "label": "regulation 1365/2000", "shape": "dot", "size": 10, "title": "regulation 1365/2000 Neighbors:\u003cbr\u003edirective 2002/12/ec\u003cbr\u003edecision 1999/468/ec\u003cbr\u003edirective 90/619/eec\u003cbr\u003edirective 2000/64/ec\u003cbr\u003edirective 85/611/eec\u003cbr\u003eregulation 1999/468\u003cbr\u003edirective 73/239/eec\u003cbr\u003edirective 93/22/eec\u003cbr\u003eregulation 92/96\u003cbr\u003edirective 91/675/eec\u003cbr\u003edirective 2001/65/ec\u003cbr\u003edirective 84/253/eec\u003cbr\u003edirective 1999/468/ec\u003cbr\u003edirective 79/267/eec\u003cbr\u003edirective 95/26/eec\u003cbr\u003edirective 91/674/eec\u003cbr\u003eregulation 93/22\u003cbr\u003edirective 2001/108/ec\u003cbr\u003eregulation 79/267\u003cbr\u003edirective 2000/12/ec\u003cbr\u003edirective 92/96/eec\u003cbr\u003edirective 2000/28/ec\u003cbr\u003edirective 2001/34/ec\u003cbr\u003edirective 83/349/eec\u003cbr\u003eregulation 90/619\u003cbr\u003edirective 78/660/eec\u003cbr\u003edirective 2002/83/ec\u003cbr\u003edirective 2002/13/ec"}, {"color": "yellow", "group": 2, "id": "regulation 806/2003", "label": "regulation 806/2003", "shape": "dot", "size": 10, "title": "regulation 806/2003 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 1782/2003", "label": "regulation 1782/2003", "shape": "dot", "size": 10, "title": "regulation 1782/2003 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 2, "id": "regulation 186/2004", "label": "regulation 186/2004", "shape": "dot", "size": 10, "title": "regulation 186/2004 Neighbors:\u003cbr\u003eregulation 228/2004\u003cbr\u003eregulation 1982/2005\u003cbr\u003eregulation 537/2004\u003cbr\u003eregulation 565/2002"}, {"color": "yellow", "group": 3, "id": "regulation 215/2003", "label": "regulation 215/2003", "shape": "dot", "size": 10, "title": "regulation 215/2003 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 881/2002", "label": "regulation 881/2002", "shape": "dot", "size": 10, "title": "regulation 881/2002 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 467/2001", "label": "regulation 467/2001", "shape": "dot", "size": 10, "title": "regulation 467/2001 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 145/2003", "label": "regulation 145/2003", "shape": "dot", "size": 10, "title": "regulation 145/2003 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 90/619", "label": "regulation 90/619", "shape": "dot", "size": 10, "title": "regulation 90/619 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 79/267", "label": "regulation 79/267", "shape": "dot", "size": 10, "title": "regulation 79/267 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 92/96", "label": "regulation 92/96", "shape": "dot", "size": 10, "title": "regulation 92/96 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 93/22", "label": "regulation 93/22", "shape": "dot", "size": 10, "title": "regulation 93/22 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 1999/468", "label": "regulation 1999/468", "shape": "dot", "size": 10, "title": "regulation 1999/468 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2002/83/ec", "label": "directive 2002/83/ec", "shape": "dot", "size": 10, "title": "directive 2002/83/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 79/267/eec", "label": "directive 79/267/eec", "shape": "dot", "size": 10, "title": "directive 79/267/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 90/619/eec", "label": "directive 90/619/eec", "shape": "dot", "size": 10, "title": "directive 90/619/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 92/96/eec", "label": "directive 92/96/eec", "shape": "dot", "size": 10, "title": "directive 92/96/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 91/674/eec", "label": "directive 91/674/eec", "shape": "dot", "size": 10, "title": "directive 91/674/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 73/239/eec", "label": "directive 73/239/eec", "shape": "dot", "size": 10, "title": "directive 73/239/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 93/22/eec", "label": "directive 93/22/eec", "shape": "dot", "size": 10, "title": "directive 93/22/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 91/675/eec", "label": "directive 91/675/eec", "shape": "dot", "size": 10, "title": "directive 91/675/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 83/349/eec", "label": "directive 83/349/eec", "shape": "dot", "size": 10, "title": "directive 83/349/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2001/34/ec", "label": "directive 2001/34/ec", "shape": "dot", "size": 10, "title": "directive 2001/34/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 84/253/eec", "label": "directive 84/253/eec", "shape": "dot", "size": 10, "title": "directive 84/253/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 78/660/eec", "label": "directive 78/660/eec", "shape": "dot", "size": 10, "title": "directive 78/660/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 85/611/eec", "label": "directive 85/611/eec", "shape": "dot", "size": 10, "title": "directive 85/611/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2000/12/ec", "label": "directive 2000/12/ec", "shape": "dot", "size": 10, "title": "directive 2000/12/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2002/12/ec", "label": "directive 2002/12/ec", "shape": "dot", "size": 10, "title": "directive 2002/12/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2000/64/ec", "label": "directive 2000/64/ec", "shape": "dot", "size": 10, "title": "directive 2000/64/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2002/13/ec", "label": "directive 2002/13/ec", "shape": "dot", "size": 10, "title": "directive 2002/13/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2001/65/ec", "label": "directive 2001/65/ec", "shape": "dot", "size": 10, "title": "directive 2001/65/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2001/108/ec", "label": "directive 2001/108/ec", "shape": "dot", "size": 10, "title": "directive 2001/108/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 2000/28/ec", "label": "directive 2000/28/ec", "shape": "dot", "size": 10, "title": "directive 2000/28/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 95/26/eec", "label": "directive 95/26/eec", "shape": "dot", "size": 10, "title": "directive 95/26/eec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "directive 1999/468/ec", "label": "directive 1999/468/ec", "shape": "dot", "size": 10, "title": "directive 1999/468/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "decision 1999/468/ec", "label": "decision 1999/468/ec", "shape": "dot", "size": 10, "title": "decision 1999/468/ec Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 1982/2005", "label": "regulation 1982/2005", "shape": "dot", "size": 10, "title": "regulation 1982/2005 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 565/2002", "label": "regulation 565/2002", "shape": "dot", "size": 10, "title": "regulation 565/2002 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 228/2004", "label": "regulation 228/2004", "shape": "dot", "size": 10, "title": "regulation 228/2004 Neighbors:\u003cbr\u003e"}, {"color": "yellow", "group": 3, "id": "regulation 537/2004", "label": "regulation 537/2004", "shape": "dot", "size": 10, "title": "regulation 537/2004 Neighbors:\u003cbr\u003e"}]);
        edges = new vis.DataSet([{"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 1913/2005", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 2759/75", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 2771/75", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 2777/75", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 1254/1999", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 1255/1999", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 2529/2001", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 1365/2000", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 806/2003", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 1782/2003", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1913/2005", "to": "regulation 186/2004", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 2529/2001", "to": "regulation 215/2003", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 2529/2001", "to": "regulation 881/2002", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 2529/2001", "to": "regulation 467/2001", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 2529/2001", "to": "regulation 145/2003", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "regulation 90/619", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "regulation 79/267", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "regulation 92/96", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "regulation 93/22", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "regulation 1999/468", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2002/83/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 79/267/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 90/619/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 92/96/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 91/674/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 73/239/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 93/22/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 91/675/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 83/349/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2001/34/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 84/253/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 78/660/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 85/611/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2000/12/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2002/12/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2000/64/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2002/13/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2001/65/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2001/108/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 2000/28/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 95/26/eec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "directive 1999/468/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 1365/2000", "to": "decision 1999/468/ec", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 186/2004", "to": "regulation 1982/2005", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 186/2004", "to": "regulation 565/2002", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 186/2004", "to": "regulation 228/2004", "weight": 5}, {"arrows": "to", "color": "blue", "from": "regulation 186/2004", "to": "regulation 537/2004", "weight": 5}]);

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
</html>
"""