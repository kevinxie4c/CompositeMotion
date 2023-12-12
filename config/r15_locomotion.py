env_cls = "ICCGANR15"
env_params = dict(
    episode_length = 300,
    motion_file = "assets/motions/r15/walk_run.json"
)

training_params = dict(
    max_epochs = 10000,
    save_interval = 2000,
    terminate_reward = -1
)

discriminators = {
    "_/full": dict(
        parent_link = None,
    )
}
