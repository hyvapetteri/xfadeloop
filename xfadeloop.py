# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:29:24 2017

@author: hyvapetteri
"""

import numpy as np

def seamless(snd, fs, xfade_s=0.5, mode="linear"):
    '''Make a no-glitch loopable sound
    
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
        
    The output sound will be xfade_s seconds shorter than the input.
    
    Keyword arguments:
    snd -- a 1-dim numpy array representation of a sound
    fs -- sampling frequency
    xfade_s -- the crossfade time in seconds (default: 0.5 sec)
    mode -- crossfade shape: "linear", "sqrt", or "cos"
    '''
    
    xfade_len = fs * xfade_s
    xfade = np.zeros((xfade_len,))
    if (mode == "linear"):
        xfade = np.linspace(0, 1, xfade_len)
    elif (mode == "sqrt"):
        xfade = np.sqrt(np.linspace(0, 1, xfade_len))
    elif (mode == "cos"):
        xfade = np.cos(np.linspace(0, np.pi/2, xfade_len))
        xfade = xfade[::-1]

    split_i = snd.shape[0]/2
    len_end = snd[split_i:].shape[0]
    
    cont_snd = np.zeros((snd.shape[0] - xfade_len,))

    snd[:xfade_len] = xfade * snd[:xfade_len]
    snd[-xfade_len:] = xfade[::-1] * snd[-xfade_len:]
    
    cont_snd[:len_end] = snd[split_i:]
    cont_snd[(len_end - xfade_len):] += snd[:split_i]
    
    return cont_snd