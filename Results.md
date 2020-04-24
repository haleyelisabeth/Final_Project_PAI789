#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:11:08 2020

@author: Shimanoduraace
"""

RESULTS


(1) The first regression shows a very weak positive or no correlation between 
the number of deaths on the date that the stay at home order was implemented 
and the predicted total deaths for each state (each normalized by population). 
Becaue the number of deaths were very low for many states when stay at home 
orders were implemented, however, the data may not accurately represent how 
widespread the pandemic was before states responded by implementing a stay at
home order. 

(2) Therefore, I made another regression looking at the number of cases
on the date that the stay at home order was implemented and the predicted total
number of deaths (both normalized for population). In this case the regression
shows a fairly positive slope meaning that the number of cases on the date that 
the stay at home order was implemented is positively correlated with the total
number of deaths. This could be evidence that states that waited longer in terms
of caseloads to implement stay at home orders will have a higher fatality 
rate than states that implemented stay at home orders sooner. 

(3)The third regression shows a weak positive correlation between the number of 
cases on the date that the stay at home orders were implemented and the duration
of social distancing measures according to IHME. In this case, states that had 
a higher number of cases before implementing stay at home orders will likely 
have to endure social distancing measures longer than states that implemented 
social distancig measures sooner. 

Note: 

States that did implement statewide stay at home orders were dropped from 
the dataset and so these states are not counted in the models. These states are
Arkansas, Connecticut, Iowa, Kentucky, Massachusetts, Nebraska, New Mexico, 
North Dakota, Oklahoma, South Dakota, Utah and Wyoming. While all states have 
closed educational facilities, I chose to focus on the implementation of stay
at home orders because there was far more variation in when stay at home orders
were implemented between states. 

Moreover, the projected 'end' date is referring to the relaxing of social 
distancing methods and not necessarily the end of stay at home orders. This 
could make the data less relevant in evaluating the implementation of stay at
home orders.

Lastly, the projections from IHME are predictions and due to the highly evolving
nature of the pandemic and the continued variation in governer's responses, the
'end' date of social distancing measures may differ in reality as well as the 
total predicted deaths. 
