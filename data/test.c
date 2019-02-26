void pwmTask(uint32_t pulse_width, uint32_t period)
{
    uint32_t time_on = pulse_width;
    uint32_t time_off = period - pulse_width;
    while (1){
        pwm_output = 1;
        sleep(time_on);
        pwm_output = 0;
        sleep(time_off);
    }
}