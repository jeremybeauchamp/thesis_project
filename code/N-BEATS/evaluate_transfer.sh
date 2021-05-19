mkdir transfer_learning

mkdir -p transfer_learning/carbs
cp carbs_models/*.model .

nice python testing.py --scenario 'carbs' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv results.json transfer_learning/carbs

mkdir -p transfer_learning/bolus
cp bolus_models/*.model .

nice python testing.py --scenario 'bolus' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv results.json transfer_learning/bolus

mkdir -p transfer_learning/combo
cp combo_models/*.model .

nice python testing.py --scenario 'combo' --case 'unrestricted' --combined 'False' --runs 10 > out.log 2> error.log
mv results.json transfer_learning/combo
