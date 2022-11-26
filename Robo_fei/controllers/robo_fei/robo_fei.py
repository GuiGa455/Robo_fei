from controller import Robot

def robot_run(robot):
    
    timestep = int(robot.getBasicTimeStep())
    m_speed = 25 #velociadade do motor, melhor velocidade com a melhor precisão = 25, mais q isso o robo fica maito instavel e fora de rota
    #seta motores do robo
    m_esquerdo = robot.getDevice('left wheel motor')
    m_direito = robot.getDevice('right wheel motor')
    
    #seta velocidade de rodagem dos motores esquerdo e direito
    m_esquerdo.setPosition(float('inf'))
    m_esquerdo.setVelocity(0.0)
    
    m_direito.setPosition(float('inf'))
    m_direito.setVelocity(0.0)
    
    #ativa os sensores de proximidade do robo
    prox_sensor = []
    for ind in range(8):
        sensor = 'ps' + str(ind)
        prox_sensor.append(robot.getDistanceSensor(sensor))
        prox_sensor[ind].enable(timestep)
    
    
    while robot.step(timestep) != -1:
        for ind in range(8):
            print("ind: {}, val: {}".format(ind, prox_sensor[ind].getValue()))
        
        #sensor da parede esquerda
        leftwall = prox_sensor[6].getValue() > 80
        #sensor da frente 
        frontwall = prox_sensor[7].getValue() > 80
        #sensor do canto
        leftcorner = prox_sensor[6].getValue() > 80

        #velocidade do motor esquerdo
        l_speed = m_speed
        #velocidade do motor direito
        r_speed = m_speed
        
        #define os parametros para o robo fazer as curvas quando detectar uma parede
        if frontwall:
            print("parede a frente")
            l_speed = m_speed
            r_speed = -m_speed
        else:
            if leftwall:
                print("parede a esquerda")
                l_speed = -m_speed
                r_speed = m_speed
            else:
                l_speed = m_speed/8
                r_speed = m_speed
            if leftcorner:
                l_speed = m_speed
                r_speed = m_speed/8  
                
                
        #seta a velocidade de cada motor
        m_esquerdo.setVelocity(l_speed)
        m_direito.setVelocity(r_speed)
    
        pass
        
if __name__ == '__main__':

    robot = Robot()
    robot_run(robot)
  






  