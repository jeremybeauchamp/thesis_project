mkdir all_times_evaluated

mkdir -p all_times_evaluated/carbs
cp carbs_models/*.model .

nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv results.json all_times_evaluated/carbs/30_results.json
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv results.json all_times_evaluated/carbs/45_results.json
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv results.json all_times_evaluated/carbs/60_results.json
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv results.json all_times_evaluated/carbs/75_results.json
nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv results.json all_times_evaluated/carbs/90_results.json

mkdir -p all_times_evaluated/bolus
cp bolus_models/*.model .

nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv results.json all_times_evaluated/bolus/30_results.json
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv results.json all_times_evaluated/bolus/45_results.json
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv results.json all_times_evaluated/bolus/60_results.json
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv results.json all_times_evaluated/bolus/75_results.json
nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv results.json all_times_evaluated/bolus/90_results.json

mkdir -p all_times_evaluated/combo
cp combo_models/*.model .

nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 30 > out.log 2> error.log
mv results.json all_times_evaluated/combo/30_results.json
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 45 > out.log 2> error.log
mv results.json all_times_evaluated/combo/45_results.json
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 60 > out.log 2> error.log
mv results.json all_times_evaluated/combo/60_results.json
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 75 > out.log 2> error.log
mv results.json all_times_evaluated/combo/75_results.json
nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 --time 90 > out.log 2> error.log
mv results.json all_times_evaluated/combo/90_results.json
