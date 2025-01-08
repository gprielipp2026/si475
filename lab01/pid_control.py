import rclpy, math, time 
from rclpy.node import Node 

from std_msgs.msg import Float32
from irobot_create_msgs.msg import WheelTicks 
from geometry_msgs.msg import Twist 
from rclpy.qos import qos_profile_sensor_data


class PID(Node): 
    def __init__(self): 
        super().__init__("PID") 
        # connect to topic that controls the wheels 
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10) 

        # subscriber to read the wheel ticks 
        self.subscriber = self.create_subscription(WheelTicks, '/wheel_ticks', self.tick_callback, qos_profile_sensor_data) 

        # subscriber to drive a distance.  You should implement two more subscribers: one to turn an angle, and 
        # another to drive in a square three times.  
        # To publish a message to the drive topic from the command line, use 
        # ros2 topic pub --once /distance std_msgs/Float32 "data: 1.0"
        # Change the 1.0 to whatever distance you want the robot to drive.  Keep in mind 
        # that you will need the quotes. 
        self.drive_sub = self.create_subscription(Float32, '/distance', self.drive, qos_profile_sensor_data) 

    # set class variables that hold the number of ticks from left and right.  You will also need to figure 
    # out what zero is.  So, at time t=0, store the current values as the starting point, and then 
    # subtract the starting point from the values.  
    def tick_callback(self, msg): 
        pass
    # Implement the pid controller here.  use the tick values from tick_callback to compute the 
    # new velocity, and then publish the velocity on self.publisher 
    def pid(self): 
        pass
    # drive a given distance in meters.  Once the driven distance is close enough to the 
    # desired distance, stop the robot by publishing a Twist message of all zeros.  
    def drive(self, distance): 
        pass


# main is basically bolerplate code.  You only need to change 
# the class you instantiate 
def main(args=None):
    # initialize all ROS Python machinery 
    rclpy.init(args=args)

    # instantiate your class 
    node = PID()

    # this runs your class in an infinite loop until 
    # either your code crashes, or you press Ctlr-C 
    rclpy.spin(node)

    # gracefully clean up 
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
