function renderTime() {
	// body...
	//Date

	var mydate = new Date;
	var year = mydate.getYear();
	if(year<1000)
	{
		year+=1900;
	}
	var day = mydate.getDay();
	var month = mydate.getMonth();
	var daym = mydate.getDate();
	var dayArray = new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
	var monthArray = new Array("January","February","March","April","May","June","July","August","September","August","October","November","December");


	//Time
	var currentTime = new Date();
	var h = currentTime.getHours();
	var min = currentTime.getMinutes();
	var s = currentTime.getSeconds();

	if(h==24)
	{
		h = 0;
	}
	else if(h>12)
	{
		h = h-0;
	}

	if(h<10)
	{
		h = '0' + h;
	}
	if(min<10)
	{
		min = '0' + min;
	}
	if(s<10)
	{
		s = '0' + s;
	}

	var myClock = document.getElementById("clockDisplay") ;
	myClock.textContent = " " + dayArray[day] + " " + daym + " " + monthArray[month] + " " + year + " " + h + ":" + min + ":" +s;
	document.getElementById('clockDisplay').style.color="white";

	setTimeout("renderTime()",1000);
 }renderTime();