import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



#experiment_ID distribution chart
objects = ('Single experiment runs', 'Multiple experiment runs')
y_pos = np.arange(len(objects))
num_runs = [3471647, 164200]

plt.bar(y_pos, num_runs, align='center', alpha=0.50)
plt.xticks(y_pos, objects)
plt.xlabel('Experiment Runs')
plt.ylabel('Number of runs')
plt.title('Distribution of experiment runs')
plt.tight_layout()
plt.show()

#study_ID distribution chart
objects = ('Single study runs', 'Multiple study runs')
y_pos = np.arange(len(objects))
num_runs = [36530, 76453]

plt.bar(y_pos, num_runs, align='center', alpha=0.50)
plt.xticks(y_pos, objects)
plt.xlabel('Study Runs')
plt.ylabel('Number of runs')
plt.title('Distribution of study runs')
plt.show()

objects = ('Single submission runs', 'Multiple submission runs')
y_pos = np.arange(len(objects))
num_runs = [311564, 89892]

plt.bar(y_pos, num_runs, align='center', alpha=0.50)
plt.xticks(y_pos, objects)
plt.xlabel('Submission Runs')
plt.ylabel('Number of runs')###########################
plt.title('Distribution of submission runs')
plt.tight_layout()
plt.show()




#single runs:
#exp      study  submission
#3471647 #36530  #311564
#multiples runs:
#164200 #76453 #89892
