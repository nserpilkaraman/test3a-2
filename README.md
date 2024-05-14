#PyTest Decoratorleri

**PyTest :** Testlerin yazılması ve yürütülmesi için popüler bir Python kütüphanesidir.

**Decoratorlar :** PyTestte yaygın olarak kullanılan bir özelliktir. Test fonksiyonlarının veya fixtureların davranışlarını değiştirmek için kullanılırlar. 


**1)@pytest.fixture :** Testlerin çalışması için gerekli verileri veya kaynakları sağlayan fixtureları tanımlamak için kullanılır. Bu fixturelar testler arasında paylaşılabilir, böylece tekrarlayan kod yazma ihtiyacı azaltılır.

**Örnek:** import pytest
**@pytest.fixture**
def some_resource():
    resource = SomeResource()
    # Resource setup
    yield resource
    # Resource teardown
    
**2)@pytest.mark.skip :** Bu decorator, belirli bir testi atlamak için kullanılır. Örneğin, hâlâ geliştirme aşamasında olan bir işlev üzerinde çalışırken geçici olarak çalışmayan bir testi atlamak isteyebilirsiniz.

**Örnek:** import pytest **@pytest.mark.skip**(reason="Not implemented yet")
def test_something():
    # Test implementation
    pass
    
**3)@pytest.mark.parametrize :** Aynı test fonksiyonunu farklı test verileriyle çalıştırmak için kullanılır. Bu sayede kod tekrarı önlenir ve test kapsamı genişletilebilir. 

**Örnek:** import pytest
**@pytest.mark.parametrize**("input, expected", [
    (1, 2),
    (2, 3),
    (3, 4)
])
def test_increment(input, expected):
    assert increment(input) == expected
    
**4)@pytest.mark.xfail:** Bir testin şu an için başarısız olması bekleniyorsa kullanılır. Bu decorator ile işaretlenen testler çalıştırılır ancak başarısız sayılmaz. Raporlarda "expected failure" (beklenen başarısızlık) olarak işaretlenir. 

**Örnek:** import pytest **@pytest.mark.xfail**
def test_something():
    # Test implementation that is expected to fail
    pass

**5)@pytest.mark.order :** Testlerin belirli bir sırayla çalışmasını sağlamak için kullanılır. Bu decoratorın kullanımı genellikle tavsiye edilmez.Testlerin birbirine bağımlı olmaması daha iyi bir yaklaşımdır. Testlerin her zaman rastgele sırayla çalıştırılmasını önerir ve testlerin birbirinden bağımsız olması gerektiğini savunur. Böylece testlerin birbirinden etkilenmesi önlenir ve test sonuçları daha güvenilir hale gelir.

**Örnek:** import pytest **@pytest.mark.order**(1)
def test_first():
    assert True
@pytest.mark.order(2)
def test_second():
    assert True
@pytest.mark.order(3)
def test_third():
    assert True
    
**6)@pytest.mark.timeout :** Belirli bir testin maksimum çalışma süresini belirlemek için kullanılır. Bu, testlerin belirli bir süre içinde tamamlanmasını sağlar ve potansiyel olarak sonsuz döngüler veya beklenmedik uzun süreli işlemler gibi sorunlardan kaçınmanıza yardımcı olur.

**Örnek:** import time
import pytest
@pytest.mark.timeout(2)  # 2 saniyeden uzun sürerse test başarısız olur
def test_slow_operation():
    time.sleep(3)  # 3 saniye bekleyin
