### Main file for UGV








def run_GroundTest():
    while(rospy.get_param('/lightswitch'==True)):

        #2) RECONFIGURE
        if(rospy.get_param('/ugv/mode'=='reconfig')):

            #Grab List of waypoints and control the vehicle to them
            x_waypoints = rospy.get_param('/ugv/waypoints')
            y_waypoints = rospy.get_param('/ugv/waypoints')


            print(waypoints)

            for target in waypoints:

                #input the target into the PID controller
                #grab the current location from the localization software


            pass
        else:
            pass








def run():
    #System Mode ('IPAS', 'Localize', 'Flight_Test', 'Ground_Test')
    #Selected mode determined from rosparam values
    mode = rospy.get_param('/mode')

    if(mode=='IPAS'):
        run_IPAS()
    elif(mode=='Localize'):
        run_Localize()
    elif(mode=='Flight_Test'):
        pass#run_FlightTest()
    elif(mode=='Ground_Test'):
        run_GroundTest()
    elif(mode=='IPAS_Sim'):
        pass #Drone not required
    else:
        print('Failed to initialize')



if __name__ == "__main__":

    initialize()
    run()
