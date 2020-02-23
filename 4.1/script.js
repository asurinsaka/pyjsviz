var chartCircles = function(data) {

	var chart = d3.select('#chart');
	chart.attr('height', data.height).attr('width', data.width)
	chart.selectAll('circle').data(data.circles)
		.enter()
		.append('circle')
		.attr('cx', function(d) { return d.x })
		.attr('cy', function(d) { return d.y })
		.attr('r', function(d) { return d.r });
};

var data = {
	width: 300, height: 150,
	circles: [
		{'x': 50, 'y': 30, 'r': 20},
		{'x': 70, 'y': 80, 'r': 10},
		{'x': 160, 'y': 60, 'r': 10},
		{'x': 200, 'y': 100, 'r': 5},
	]
};

chartCircles(data);
