import matplotlib.pyplot as plt
import os


# barplots
from barplots.barplot_runtime_summary import generate_plot1

#grouped barplots
from barplots.groupedbarplot_counts_correct_incorrect_for_pasda_diff_each_timeout import generate_plot2
from barplots.groupedbarplot_runtime_sorted_by_timeout import generate_plot3
from barplots.groupedbarplot_runtime_sorted_by_tool import generate_plot4

from barplots.groupedbarplot_cases_ARDiffbase_sorted_by_timeout import generate_plot21
from barplots.groupedbarplot_cases_ARDiffdiff_sorted_by_timeout import generate_plot22
from barplots.groupedbarplot_cases_SEbase_sorted_by_timeout import generate_plot23
from barplots.groupedbarplot_cases_SEdiff_sorted_by_timeout import generate_plot24
from barplots.groupedbarplot_cases_DSEbase_sorted_by_timeout import generate_plot25
from barplots.groupedbarplot_cases_DSEdiff_sorted_by_timeout import generate_plot26
from barplots.groupedbarplot_cases_PASDAdiff_sorted_by_timeout import generate_plot27

#boxplots
from boxplots.boxplot_runtime_each_timeout_tool import generate_plot5
from boxplots.boxplot_runtime_each_tool_timeout import generate_plot6

#lineplots
from lineplots.lineplot_corect_cases_ARDiffbase_by_runtimeout import generate_plot7
from lineplots.lineplot_correct_cases_ARDiffdiff_by_runtimeout import generate_plot8
from lineplots.lineplot_correct_cases_DSEbase_by_runtimeout import generate_plot9
from lineplots.lineplot_correct_cases_DSEdiff_by_runtimeout import generate_plot10
from lineplots.lineplot_correct_cases_PASDAdiff_by_runtimeout import generate_plot11
from lineplots.lineplot_correct_cases_SEbase_by_runtimeout import generate_plot12
from lineplots.lineplot_correct_cases_SEdiff_by_runtimeout import generate_plot13

from lineplots.lineplot_correct_cases_timeout_10 import generate_plot14
from lineplots.lineplot_correct_cases_timeout_30 import generate_plot15
from lineplots.lineplot_correct_cases_timeout_90 import generate_plot16
from lineplots.lineplot_correct_cases_timeout_300 import generate_plot17
from lineplots.lineplot_correct_cases_timeout_900 import generate_plot18
from lineplots.lineplot_correct_cases_timeout_3600 import generate_plot19
from lineplots.lineplot_correct_cases_ARDiffbase_PASDAdiff_timeout_10 import generate_plot20


def main():

    generate_plot1()
    generate_plot2()
    generate_plot3()
    generate_plot4()
    generate_plot21()
    generate_plot22()
    generate_plot23()
    generate_plot23()
    generate_plot24()
    generate_plot25()
    generate_plot26()
    generate_plot27()
    generate_plot5()
    generate_plot6()
    generate_plot7()
    generate_plot8()
    generate_plot9()
    generate_plot10()
    generate_plot11()
    generate_plot12()
    generate_plot13()
    generate_plot14()
    generate_plot15()
    generate_plot16()
    generate_plot17()
    generate_plot18()
    generate_plot19()
    generate_plot20()

   
  

if __name__ == "__main__":
    main()
