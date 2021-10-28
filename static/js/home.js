function searchdata() {
            var input, table, tr, td, filter;
            input = document.getElementById("searchid1")
            filter = input.value();
            table = document.getElementById("box1")
            tr = table.getElementByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementByTagName("td")[1];
                if (td) {
                    displaydata = td.innerText;
                    if (displaydata.indexOf(filter) > -1) {
                        tr[i].style.display = ""
                    } else {
                        tr[i].style.display = "none"
                    }
                }
            }

        }

$(function() {

    var $populationChart = $("#population-chart");
    $.ajax({
        url: $populationChart.data("url"),
        success: function(data) {

            var ctx = $populationChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'AmountOutstanding',
                        backgroundColor: 'blue',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,

                    }
                }
            });

        }
    });

});

$(function() {

    var $populationChart = $("#newnpachar");
    $.ajax({
        url: $populationChart.data("url"),
        success: function(data) {

            var ctx = $populationChart[0].getContext("2d");

            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'recovery',
                        backgroundColor: 'blue',
                        data: data.data
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,

                    }
                }
            });

        }
    });

});