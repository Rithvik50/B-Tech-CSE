rm *.log
rm *.state_machine
rm *.storage
touch node1_CUSTOMLOG.log node2_CUSTOMLOG.log node3_CUSTOMLOG.log

# Create a new tmux session
tmux new-session -d -s PES2UG22CS451

# Split the window horizontally
tmux split-window -h

# Split the top pane vertically into two panes (66% and 33%)
tmux split-window -v -p 66
tmux split-window -v

# Select the left-top pane
tmux select-pane -t 0

# Split the left-top pane vertically into two panes (66% and 33%)
tmux split-window -v -p 66
tmux split-window -v

# Attach to the tmux session
tmux attach-session -t PES2UG22CS451
