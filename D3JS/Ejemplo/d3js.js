

circleData = [[10, "rgb(246, 239, 247)"], [15, "rgb(189,201,225)"],

    [20, "rgb(103,169,207)"], [25, "rgb(28,144,153)"], [30, "rgb(1,108,89)"]];

//Select the div element
selectExample = d3.select("#data_example2");

//We'll select all the circle from within the selected <div> element
selectExample.selectAll("circle")
    .data(circleData)
    .attr("r", function(d){return d[0]})
    .style("fill", function(d){return d[1]});