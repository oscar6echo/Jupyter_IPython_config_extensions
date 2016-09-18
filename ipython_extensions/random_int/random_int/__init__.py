
import random
from IPython.core.magic import magics_class, line_magic, Magics

random.seed(123456)


def generate_rnd_int(max):
    return random.randint(0, max)


@magics_class
class RandomInt(Magics):

    @line_magic
    def random_int(self, line=''):
        """Show information about versions of modules.
        Usage:
            %random_int [optional max - else max=100]
        """

        try:
            max = int(line)
        except:
            max = 100
        self.nb = generate_rnd_int(max=max)

        return self

    def _repr_html_(self):

        html = "<b>"
        html += str(self.nb)
        html += "</b>"

        return html


def load_ipython_extension(ipython):
    ipython.register_magics(RandomInt)
    print("extension random_int loaded")


def unload_ipython_extension(ipython):
    del ipython.magics_manager.magics['cell']['random_int']
    print("extension random_int unloaded")
