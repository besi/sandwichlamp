from machine import Pin, UART
import utime
import ld2410

boardled = Pin(13, Pin.OUT)
boardled.off()

print('-----------CONFIGURATION----------------')
uart1 = UART(1, baudrate = 256000, tx=Pin(27), rx=Pin(12), timeout = 3)
human_sensor = ld2410.LD2410(uart1)
human_sensor.enable_config()
#human_sensor.Maximum_distance_gate_and_unoccupied_duration_parameters_configuration(2,2,50) # 2-->8,2-->8,0-->65535 
#human_sensor.read_parameter()
#human_sensor.distance_gate_sensitivity_configuration(1,4,4)
human_sensor.read_firmware_version()
#human_sensor.set_serial_port_baud_rate(0x0007) #0007 --> 256000 ,  0x0005-->115200
#human_sensor.restore_factory_settings()
#human_sensor.reboot_module() #--> end_config failure
#human_sensor.bluetooth_setting(0x0001)  #0x0001-->ON 0x0000-->OFF 
human_sensor.get_mac_address()
#human_sensor.set_bluetooth_password()
human_sensor.distance_resolution_setting(0x0000)
#human_sensor.query_distance_resolution_setting()
human_sensor.end_config()
#human_sensor.enable_engineering_mode()
#human_sensor.end_engineering_mode()

utime.sleep(5)

print('-----------DECTECTION----------------')
while True: 
    human_sensor.send_command_report_data()
    #human_sensor.print_meas()
    human_sensor.human_detection(boardled,50,50)
    utime.sleep(.1)
