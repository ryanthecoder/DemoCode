beringHeight = 5;
beringRadius = 10;
axilRadius = 5;
carSize = [50,200,100];
circularRes = 100;
isCenter = false;

difference()
{
	color ([255,255,0])
	cube (carSize, center=isCenter);

	translate([(carSize[0]/2),(carSize[1]/10), -1]) 
		cylinder(h=(carSize[2]+2),r=axilRadius, $fn=circularRes, center=isCenter);
	
	translate([(carSize[0]/2),(carSize[1]/10),(carSize[2]/10)]) 
		cylinder(h=beringHeight,r=beringRadius,$fn=circularRes, center = isCenter);
	translate([(carSize[0]/2),(carSize[1]/10),(carSize[2]-carSize[2]/10)-beringHeight]) 
		cylinder(h=beringHeight,r=beringRadius,$fn=circularRes, center = isCenter);
	
	translate([(carSize[0]/2),(carSize[1]-(carSize[1]/10)),-1]) 
		cylinder(h=carSize[2]+2,r=axilRadius,$fn=circularRes, center = isCenter);

	translate([(carSize[0]/2),(carSize[1]-(carSize[1]/10)),carSize[2]/10])
		cylinder(h=beringHeight,r=beringRadius,$fn=circularRes, center = isCenter);
	translate([(carSize[0]/2),(carSize[1]-(carSize[1]/10)),(carSize[2]-carSize[2]/10)-beringHeight])
		cylinder(h=beringHeight,r=beringRadius,$fn=circularRes, center = isCenter);

}