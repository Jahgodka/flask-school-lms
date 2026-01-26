function initCharts() {
	new Chart(document.getElementById("gradesDistributionChart"), {
		type: "doughnut",
		data: {
			labels: ["5", "4", "3", "2"],
			datasets: [
				{
					data: [gradeDist["5"], gradeDist["4"], gradeDist["3"], gradeDist["2"]],
					backgroundColor: ["#4bc0c0", "#36a2eb", "#ffcd56", "#ff6384"],
				},
			],
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		},
	});
}

if (document.readyState === "complete") {
	initCharts();
} else {
	document.addEventListener("DOMContentLoaded", initCharts);
}