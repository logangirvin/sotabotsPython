import javax.swing.JLabel;

import edu.wpi.first.smartdashboard.gui.StaticWidget;
import edu.wpi.first.smartdashboard.properties.Property;


public class Printer extends StaticWidget{
	static JLabel xLabel    = new JLabel();
	static JLabel distanceLabel = new JLabel();
	static JLabel aimLabel 	 = new JLabel();
	static JLabel targetLabel   = new JLabel();
	
	@Override
	public void init() {
			
		add(xLabel);
		add(distanceLabel);
		add(aimLabel);
		add(targetLabel);
		
	}

	@Override
	public void propertyChanged(Property arg0) {
		
	}
	
	public static void refresh() {
		distanceLabel.setText("DISTANCE: " + Vision.distance);
		xLabel.setText("AVG DISTANCE: " + Vision.avgDistance);
		aimLabel.setText("AIM COORDINATE: " + Vision.centerAim);
		targetLabel.setText("AIM AVG: " + Vision.avgCenterAim);
	} 

}
