"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <body class="dash-template">
            <script>
	            const ctx = document.getElementById("the_vibe").getContext("2d");
	            const the_vibe_chart = new Chart(ctx, {
			        type: 'pie',
                    data: {
                    labels: {{ gate }},
                        datasets: [{
                            label: "The Song Vibes",
                            data: {{ boat }},
                            backgroundColor: ['#5DA5DA ', '#FAA43A', '#60BD68',
                                '#B276B2', '#E16851', '#FB8267', '#4200EA', '#5AEB00', '#EB0033',
                            '#EBDF00', '#EB00A8', '#EB0033','#00EB9C', '#DF00EB', '#0046EB',
                            '#A400EB', '#00BCEB', '#A400EB', '#8D8E38', '#00BCEB','#EB7500',
                            '#EB0000', '#00EBEB', '#00EB9C', '#009CEB', '#0000EB', '#7500EB'],

                            borderWidth: 1,
                            hoverBorderColor: "black",
                            hoverBorderWidth: 2,
                            hoverBackgroundColor: 'rgba(154, 245, 140)',
                            pointHoverRadius: 5
                        }],
                    },
                    options: {
                            title: {
                                display: true,
                                text: "The Song Vibes",
                                fontSize: 20,
                            },
                            legend: {
                                position: "right",
                                labels: {
                                    fontColor: "gray"
                                },
                                display: true,
                            },

                            elements: {
                                hitRadius: 3,
                            }
                    }
                });
	</script>
        </body>
    </html>
"""