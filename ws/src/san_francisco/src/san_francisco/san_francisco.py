import rospy
from robonomics_lighthouse.msg import Ask, Bid
from std_msgs.msg import String

class SanFrancisco:
    model = 'QmYYkm3FkBCbWcPMDWRbqrgAZ53t2VgPmqGjVc23RKmRr8'

    def __init__(self):
        rospy.init_node('san_francisco_node')
        pub = rospy.Publisher('liability/infochan/signing/bid', Bid, queue_size=10)

        def create_offer(m):
            rospy.loginfo('incoming ask')
            if m.model == self.model:
                offer = Bid()
                offer.model = self.model
                offer.objective = 'QmPGhwtN1ndML9iwDYPtMZeqNyQWQPaTRT981MQyZUZbwP'
                offer.token = '0xbD949595eE52346c225a19724084cE517B2cB735'
                offer.cost = 1
                offer.lighthouseFee = 0
                offer.deadline = m.deadline + 1000
                pub.publisher(offer)
        rospy.Subscriber('liability/infochan/incoming/ask', Ask, create_offer)

        def output_string(m):
            lines = m.data.splitlines()
            for s in lines:
                rospy.loginfo(s)
                rospy.sleep(1)
        rospy.Subscriber('san_francisco_data', String, output_string)

    def spin(self):
        rospy.spin()    
