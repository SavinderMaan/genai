var chartDom = document.getElementById('chart');
var myChart = echarts.init(chartDom);

var option = {
    xAxis: {
        type: 'category',
        data: ids
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: values,
        type: 'line',
        smooth: true,
        areaStyle: {}
    }]
};

myChart.setOption(option);

$(document).ready(function () {
    $('#dataTable').DataTable();
});

