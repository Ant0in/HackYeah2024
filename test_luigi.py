import luigi

class MyTask1(luigi.Task):
    x = luigi.IntParameter()

    def requires(self):
        return MyTask2(self.x)

    def run(self):
        print(self.x + self.y)


class MyTask2(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=1)
    z = luigi.IntParameter(default=2)

    def run(self):
        return self.x + self.y + self.z

if __name__ == '__main__':
    luigi.build([MyTask1(), MyTask2(x=15, z=3)], local_scheduler=True)