#!/bin/bash

mkdir carbs_transfer_time

mkdir carbs_transfer_time/carbs_30
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv *.model carbs_transfer_time/carbs_30
cp *.json carbs_transfer_time/carbs_30

mkdir carbs_transfer_time/carbs_45
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv *.model carbs_transfer_time/carbs_45
cp *.json carbs_transfer_time/carbs_45

mkdir carbs_transfer_time/carbs_60
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv *.model carbs_transfer_time/carbs_60
cp *.json carbs_transfer_time/carbs_60

mkdir carbs_transfer_time/carbs_75
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv *.model carbs_transfer_time/carbs_75
cp *.json carbs_transfer_time/carbs_75

mkdir carbs_transfer_time/carbs_90
nice python run.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv *.model carbs_transfer_time/carbs_90
cp *.json carbs_transfer_time/carbs_90

mkdir bolus_transfer_time

mkdir bolus_transfer_time/bolus_30
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv *.model bolus_transfer_time/bolus_30
cp *.json bolus_transfer_time/bolus_30

mkdir bolus_transfer_time/bolus_45
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv *.model bolus_transfer_time/bolus_45
cp *.json bolus_transfer_time/bolus_45

mkdir bolus_transfer_time/bolus_60
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv *.model bolus_transfer_time/bolus_60
cp *.json bolus_transfer_time/bolus_60

mkdir bolus_transfer_time/bolus_75
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv *.model bolus_transfer_time/bolus_75
cp *.json bolus_transfer_time/bolus_75

mkdir bolus_transfer_time/bolus_90
nice python run.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv *.model bolus_transfer_time/bolus_90
cp *.json bolus_transfer_time/bolus_90

mkdir combo_transfer_time

mkdir combo_transfer_time/combo_30
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv *.model combo_transfer_time/combo_30
cp *.json combo_transfer_time/combo_30

mkdir combo_transfer_time/combo_45
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv *.model combo_transfer_time/combo_45
cp *.json combo_transfer_time/combo_45

mkdir combo_transfer_time/combo_60
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv *.model combo_transfer_time/combo_60
cp *.json combo_transfer_time/combo_60

mkdir combo_transfer_time/combo_75
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv *.model combo_transfer_time/combo_75
cp *.json combo_transfer_time/combo_75

mkdir combo_transfer_time/combo_90
nice python run.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv *.model combo_transfer_time/combo_90
cp *.json combo_transfer_time/combo_90
