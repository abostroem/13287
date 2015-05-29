from datetime import datetime
import os

def get_repository_path():
	current_dir = os.getcwd()
	users_path = current_dir.split('/13287')[0]
	repo_path = os.path.join(users_path, '13287')
	return repo_path

def add_date_to_plot(ax):
    today = datetime.today()
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    ax.text(xlims[1], -.06*(ylims[1] - ylims[0])+ylims[0], '{}-{}-{}'.format(today.year, today.month, today.day))
