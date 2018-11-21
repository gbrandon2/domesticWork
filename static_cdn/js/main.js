$('.Singin').click(function(){
    $('.formulario').animate({
        height: "toggle",
        'padding-top': 'toggle',
        'padding-bottom': 'toggle',
        opacity: 'toggle'
    }, "slow");
});
document.getElementById('button').addEventListener("click", function() {
		document.querySelector('.bg-modal').style.display = "flex";
	});
document.querySelector('.toggle').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});
