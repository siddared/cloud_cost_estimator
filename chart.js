document.addEventListener("DOMContentLoaded", function () {

    const chartElement =
        document.getElementById("costChart");

    if (chartElement) {

        new Chart(chartElement, {

            type: "pie",

            data: {

                labels: [
                    "EC2",
                    "S3",
                    "RDS",
                    "Transfer"
                ],

                datasets: [{

                    data: [
                        40,
                        20,
                        25,
                        15
                    ]

                }]

            }

        });

    }

});