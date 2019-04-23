use "H:\jbarg\PycharmProjects\corporate_disruptions\preprocessed\pace_delta_2 2019-04-23.dta"
xtset name year, delta(2)
xtreg recalls high_turnover_running_3 revenue_1 ceo_exit_1, fe vce(cluster name)
