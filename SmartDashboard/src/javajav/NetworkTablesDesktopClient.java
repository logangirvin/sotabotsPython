package javajav;
import edu.wpi.first.smartdashboard.robot.Robot;
import edu.wpi.first.wpilibj.networktables.*;
import edu.wpi.first.wpilibj.networktables2.*;


public class NetworkTablesDesktopClient {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		new NetworkTablesDesktopClient().run();

	}

	@SuppressWarnings("deprecation")
	private void run() {
		//NetworkTable.setClientMode()
		NetworkTable.setIPAddress("10.25.57.2");
		NetworkTable table = (NetworkTable) Robot.getTable();
		
		while (true) {
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			table.putNumber("Q", 11);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println(table.getNumber("Q"));
		}
		
	}

}
