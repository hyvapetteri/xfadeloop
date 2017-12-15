# Seamless looping
This python script converts a one-shot audio segment into a
no-glitch loopable segment.

Takes a sound and cross-fades the start and end in order
to make a continuous sound that can be looped without
a "pop"-sound due to discontinuities between the beginning
and the end of a sound.

The output sound will have the cross-fade between end and start
at the middle, and the first and last sample of the output sound
will be successive samples from the middle of the input sound:
    
    input sound:
    F-----------------AB----------------L
    
    output sound:
    B----------------L
                 \\\\\
                 F-----------------A
    
    where F and L are the first and last sample, respectively, 
    of the original sound. A and B
    are two successive samples midway through the sound,
    and the \'s indicate cross-fading.
    
