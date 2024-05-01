const events = {
	login_tab,
	register_tab,
	login_button,
	register_button,
	logout_button,
	overlay,
	startGame,
}

document.addEventListener('click', async (e) => {
	e.preventDefault();

	if (e.target.id.includes('popup'))
	{
		openPopup(e);
	}
	else if (e.target.id.includes("close_button"))
	{
		closePopup(e);
	}
	else if (e.target.id.includes("vs"))
	{
		startGame(e.target.id);
	}
	else
	{
		events[e.target.id]?.(e);
	}
});

document.addEventListener('input', async (e) => {
	e.preventDefault();

	// if (document.getElementById("error").classList.contains("hide") === false)
	hideErrorMessage();
	
	// events[`${e.target.id}_input`]?.(e);
});
