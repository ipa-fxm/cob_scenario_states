#!/usr/bin/python

import rospy
import smach
import smach_ros
import unittest

from cob_generic_states.generic_basic_states import *

class TestStates(unittest.TestCase):
	def __init__(self, *args):
		super(TestStates, self).__init__(*args)
		rospy.init_node('test_states')

	def test_initialize(self):
		# create a SMACH state machine
		SM = smach.StateMachine(outcomes=['overall_succeeded','overall_failed'])

		# open the container
		with SM:
			smach.StateMachine.add('TEST', initialize(),
				transitions={'succeeded':'overall_succeeded', 'failed':'overall_failed'})

		try:
			SM.execute()
		except:
			error_message = "Unexpected error:", sys.exc_info()[0]
			self.fail(error_message)

	def test_get_oder(self):
		# create a SMACH state machine
		SM = smach.StateMachine(outcomes=['overall_succeeded','overall_failed'])

		# open the container
		with SM:
			smach.StateMachine.add('TEST', get_order(),
				transitions={'succeeded':'overall_succeeded', 'failed':'overall_failed'})

		try:
			SM.execute()
		except:
			error_message = "Unexpected error:", sys.exc_info()[0]
			self.fail(error_message)

	def test_deliver_object(self):
		# create a SMACH state machine
		SM = smach.StateMachine(outcomes=['overall_succeeded','overall_failed'])

		# open the container
		with SM:
			smach.StateMachine.add('TEST', deliver_object(),
				transitions={'succeeded':'overall_succeeded', 'failed':'overall_failed'})

		try:
			SM.execute()
		except:
			error_message = "Unexpected error:", sys.exc_info()[0]
			self.fail(error_message)

# main
if __name__ == '__main__':
    import rostest
    rostest.rosrun('cob_generic_states', 'basic', TestStates)
