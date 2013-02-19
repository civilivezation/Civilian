//function to check last login & apply muliplier(maybe embbeded in civ/home)
//multiplyer for when logged out
var mcurrency = 1.4; 			//pull currency multiplyer
var mmilitary = 1.1;			//pull military multiplyer
var marts = 1.3;				//pull arts multiplyer
var mscience = 0.4;				//pull science multiplyer
var mfood = 1.1;				//pull food multiplyer
var multiplyers;
multiplyers[0] = mcurrency;
multiplyers[1] = mmilitary;
multiplyers[2] = marts;
multiplyers[3] = mscience;
multiplyers[4] = mfood;

var mcurrency = 1.4; 			//pull currency multiplyer
var mmilitary = 1.1;			//pull military multiplyer
var marts = 1.3;				//pull arts multiplyer
var mscience = 0.4;				//pull science multiplyer
var mfood = 1.1;				//pull food multiplyer
var multiplyers;
multiplyers[0] = mcurrency;
multiplyers[1] = mmilitary;
multiplyers[2] = marts;
multiplyers[3] = mscience;
multiplyers[4] = mfood;

var mycurrency = 1.4; 			//pull currency
var mymilitary = 1.1;			//pull military points
var myarts = 1.3;				//pull arts points
var myscience = 0.4;			//pull science points
var myfood = 1.1;				//pull food points
var mypoints;
mypoints[0] = mcurrency;
mypoints[1] = mmilitary;
mypoints[2] = marts;
mypoints[3] = mscience;
mypoints[4] = mfood;


var oldtime = (); //pull old log out date

var newtime = new Date().getTime() / 1000;

var timechange = (newtime - oldtime);

var i;
var fee[];
for (i=0; i++; i<=4){
	fee[i] = mypoints[i];
	var temp = multipyers[i]*mypoints[i];
	mypoints[i]= temp;
}
var string = "Your points have changed as follows: ");
for(i=0;i++;i<=4){
			string = string + fee[i];
			string += " has become ";
			string += mypoints[i];
		}
alert(string);

