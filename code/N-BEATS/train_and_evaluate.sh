#!/bin/bash

mkdir results

mkdir results/carbs

mkdir results/carbs/inertial
nice python run.py --scenario 'carbs' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/carbs/inertial

mkdir results/carbs/unrestricted
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/carbs/unrestricted

mkdir results/bolus

mkdir results/bolus/inertial
nice python run.py --scenario 'bolus' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/bolus/inertial

mkdir results/bolus/unrestricted
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/bolus/unrestricted

mkdir results/combo

mkdir results/combo/inertial
nice python run.py --scenario 'combo' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'inertial' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/combo/inertial

mkdir results/combo/unrestricted
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv *.model results.json run_results.json results/combo/unrestricted
