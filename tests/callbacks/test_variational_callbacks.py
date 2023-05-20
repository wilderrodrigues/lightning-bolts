from pytorch_lightning.loggers.logger import DummyLogger

from pl_bolts.callbacks import LatentDimInterpolator
from pl_bolts.models.gans import GAN


def test_latent_dim_interpolator():
    class FakeTrainer:
        def __init__(self) -> None:
            self.current_epoch = 1
            self.global_step = 1
            self.logger = DummyLogger()

    model = GAN(3, 28, 28)
    cb = LatentDimInterpolator(interpolate_epoch_interval=2)

    cb.on_train_epoch_end(FakeTrainer(), model)
