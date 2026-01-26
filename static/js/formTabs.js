function showTab(tabName) {
	document
		.querySelectorAll(".tab")
		.forEach((tab) => tab.classList.remove("active"));
	document
		.querySelectorAll("form")
		.forEach((form) => form.classList.add("hidden"));
	if (tabName === "register") {
		document.querySelector("#registerForm").classList.remove("hidden");
		document.querySelector(".tab:nth-child(1)").classList.add("active");
	} else {
		document.querySelector("#loginForm").classList.remove("hidden");
		document.querySelector(".tab:nth-child(2)").classList.add("active");
	}
}
